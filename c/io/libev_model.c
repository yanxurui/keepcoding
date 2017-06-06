/*all watcher callbacks have a similar signature
  callback arguments:
      1. event loop pointer, or use EV_P_ macro
      2. the registered watcher structure
      3. a bitset of received events
*/
static void my_cb (struct ev_loop *loop, ev_io *w, int revents)
{
    // ...
    // stop watching for events at any time by calling the corresponding stop function ev_TYPE_stop (loop, watcher *)
    ev_io_stop (w);
    // stop the event loop by `ev_break (loop, how)`
    // below causes all nested ev_run's to stop iterating
    ev_break (loop, EVBREAK_ALL);
}

// step1: create a default event loop by struct ev_loop *ev_default_loop (unsigned int flags) or via EV_DEFAULT macro.
// the flags is used to specify behaviour or backends(epoll, select, etc).
ev_loop *loop = ev_default_loop (0);

// step2: create a watcher
// each watcher has an associated watcher structure
// ev_TYPE is typedef of struct ev_TYPE
ev_io stdin_watcher;

// step3: initial the watcher with a callback by `ev_init (watcher *, callback)`.
// this callback is in invoked each time the event occurs
ev_init (&stdin_watcher, my_cb);

// step4: confgiure the watcher by `ev_TYPE_set (watcher *, ...)`, arguments are specific to the watcher type
ev_io_set (&stdin_watcher, STDIN_FILENO, EV_READ);

// step3 and step4 can be combined in one call: ev_TYPE_init(watcher *, callback, ...)

// step5: start to watch by `ev_TYPE_start (loop, watcher *)`
ev_io_start (loop, &stdin_watcher);

// now the watcher is active and actually watch out for the events
// never reinitial or reconfigure it

// step6: start handling events by `bool ev_run (loop, int flags)`
// It will ask the operating system for any new events, call the watcher callbacks, and then repeat the whole process indefinitely
ev_run (loop, 0);
