<!-- https://stackoverflow.com/a/39831043/6088837 -->
<?php
//Variables
$NumRows=30000;

$mysqli = new mysqli("127.0.0.1", "root", "", "test", 3306);
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}


//These 2 functions need to be filled in
function InitSQL()
{

}
function RunSQLQuery($Q)
{
    global $mysqli;
    $mysqli->query($Q);
}

//Run the 3 tests
InitSQL();
for($i=0;$i<4;$i++)
    RunTest($i, $NumRows);

function RunTest($TestNum, $NumRows)
{
    $TheQueries=Array();
    $DoQuery=function($Query) use (&$TheQueries)
    {
        RunSQLQuery($Query);
        $TheQueries[]=$Query;
    };

    $TableName='Test';
    $DoQuery('DROP TABLE IF EXISTS '.$TableName);
    $DoQuery('CREATE TABLE '.$TableName.' (i1 int NOT NULL AUTO_INCREMENT, i2 int NOT NULL, primary key (i1)) ENGINE=InnoDB');
    $DoQuery('INSERT INTO '.$TableName.' (i2) VALUES ('.implode('), (', range(2, $NumRows+1)).')');

    if($TestNum==0)
    {
        $TestName='Transaction';
        $Start=microtime(true);
        $DoQuery('START TRANSACTION');
        for($i=1;$i<=$NumRows;$i++)
            $DoQuery('UPDATE '.$TableName.' SET i2='.(($i+5)*1000).' WHERE i1='.$i);
        $DoQuery('COMMIT');
    }

    if($TestNum==1)
    {
        $TestName='Insert';
        $Query=Array();
        for($i=1;$i<=$NumRows;$i++)
            $Query[]=sprintf("(%d,%d)", $i, (($i+5)*1000));
        $Start=microtime(true);
        $DoQuery('INSERT INTO '.$TableName.' VALUES '.implode(', ', $Query).' ON DUPLICATE KEY UPDATE i2=VALUES(i2)');
    }

    if($TestNum==2)
    {
        $TestName='Case';
        $Query=Array();
        for($i=1;$i<=$NumRows;$i++)
            $Query[]=sprintf('WHEN %d THEN %d', $i, (($i+5)*1000));
        $Start=microtime(true);
        $DoQuery("UPDATE $TableName SET i2=CASE i1\n".implode("\n", $Query)."\nEND\nWHERE i1 IN (".implode(',', range(1, $NumRows)).')');
    }

    if($TestNum==3)
    {
        $TestName='Multi';
        $Query=Array();
        for($i=1;$i<=$NumRows;$i++)
            $Query[]='UPDATE '.$TableName.' SET i2='.(($i+5)*1000).' WHERE i1='.$i;
        $Q = implode(';', $Query);
        $TheQueries[]=$Q;
        $Start=microtime(true);
        global $mysqli;
        $mysqli->multi_query($Q);
    }

    print "$TestName: ".(microtime(true)-$Start)."<br>\n";

    file_put_contents("./$TestName.sql", implode(";\n", $TheQueries).';');
}