using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Reflection;
using System.Management.Automation;
using System.Management.Automation.Runspaces;

/// <summary>
/// This demonstrates how to
/// 1. write a hello world cmdlet that accepts arrary for a parameter (this is bad)
/// 2. call a cmdlet from itself
/// 3. run cmdlet asychronously using RunspacePool
/// </summary>
namespace ClassLibrary1
{
    /// <summary>
    /// A cmdlet call itself if the input parameter Name has multiple values
    /// </summary>
    [Cmdlet(VerbsCommon.Get, "HelloWorld")]
    public class GetHelloWorld : PSCmdlet
    {
        [Parameter(Mandatory = true, Position = 1, ValueFromPipelineByPropertyName = true)]
        public string[] Name { get; set; }

        /// <summary>
        /// execute cmdlets parallelly using RunspacePool
        /// https://docs.microsoft.com/en-us/powershell/scripting/developer/prog-guide/runspace09-code-sample?view=powershell-7
        /// </summary>
        protected override void ProcessRecord()
        {
            if (Name.Length > 1)
            {
                Dictionary<string, object> parameters = MyInvocation.BoundParameters;
                InitialSessionState initial = Runspace.DefaultRunspace.InitialSessionState;
                initial.ImportPSModule(new string[] { Assembly.GetExecutingAssembly().Location });
                using (RunspacePool rsp = RunspaceFactory.CreateRunspacePool(initial))
                {
                    rsp.SetMaxRunspaces(2);
                    rsp.Open();
                    PSDataCollection<PSObject> output = new PSDataCollection<PSObject>();
                    foreach (string n in Name)
                    {
                        parameters["Name"] = new string[] { n };

                        PowerShell ps = PowerShell.Create();
                        ps.RunspacePool = rsp;
                        ps.AddCommand(MyInvocation.InvocationName);
                        ps.AddParameters(parameters);
                        ps.BeginInvoke<PSObject, PSObject>(null, output);
                    }
                    foreach (PSObject result in output)
                    {
                        WriteObject(result);
                    }
                    rsp.Close(); // all cmdlets should have completed
                }
            }
            else
            {
                foreach (char c in Name[0].ToCharArray())
                {
                    WriteObject(c);
                    System.Threading.Thread.Sleep(1000);
                }
            }
        }
    }
}
