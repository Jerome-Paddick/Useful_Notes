Javascript
===

### Async

Js is single threaded, heavy function in call stack will `block` browser from running rest of code

JS Engine:   
- on demand execution environment, surrounding environment schedules code execution

Event Loop:   
- handles execution of multiple chunks of js  
- monitors Call Stack and pushes events from Callback Queue if Stack is empty

WEB APIs:   
- `DOM`, `AJAX`, `Timeout` etc.  
- Take requests from Event Loop and return output to Callback Queue

Job Queue:  
- Layer on top of Event Loop Queue
- Attaches functions to the end of every tick of the Event Loop Queue
- Runs Jobs later but ASAP
- Can spawn more jobs which execute before Event loop resumes


Js will split files into `blocks` and try to run them separately (functions are block units)

    var response = ajax('https://example.com/api');
    // ajax request are asynchronous
    console.log(response);
    // `response` won't have the response

simple wait -> `callback`

    ajax('https://example.com/api', function(response) {
        console.log(response); // `response` is now available
    });

On ajax request, JS Engine tells hosting env to call function when network request returned and data available  
-> Browser schedules callback by inserting it into the event loop

Promises:
- `var p = new Promise(function(resolve,reject)){};`
- `p.then(function fulfilled(){}, function rejected(err){});`
- Once resolved -> Time Independent, externally immutable objects
- Can be combined in predictable ways


    function sum(xPromise, yPromise) {
        // `Promise.all([ .. ])` takes an array of promises,
        // and returns a new promise that waits on them all to finish
        return Promise.all([xPromise, yPromise])
    
        // when that promise is resolved, let's take the
        // received `X` and `Y` values and add them together.
        .then(function(values){
            // `values` is an array of the messages from the
            // previously resolved promises
            return values[0] + values[1];
        } );
    }
    
    // `fetchX()` and `fetchY()` return promises for
    // their respective values, which may be ready
    // *now* or *later*.
    sum(fetchX(), fetchY())
    
    // we get a promise back for the sum of those two numbers.
    // now we chain-call `then(...)` to wait for the
    // resolution of that returned promise.
    
    //fullfillment handler
    .then(function(sum){
        console.log(sum);
    // rejection handler
    function(err) {
    	console.error( err ); // bummer!
    }
    });

async:
- Returns a promise
- made to simplify behaviour of promises


    // Just a standard JavaScript function
    function getNumber1() {
        return Promise.resolve('374');
    }
    // This function does the same as getNumber1
    async function getNumber2() {
        return 374;
    }



---
### Promises

Js is single threaded -> cannot run concurrent scripts

conventionally use event listeners and callbacks
    
    var img1 = document.querySelector('.img-1');
    
    img1.addEventListener('load', function() {
      // woo yey image loaded
    });
    img1.addEventListener('error', function() {
      // argh everything's broken
    });
    
js can stop executing until one of the listeners is called  
-> causes problems, events can happen before we start listening etc.

Promises are like listeners except:
1.  Can only succeed or fail once
2.  If a promise has succeeded or failed, it will return that value to a callback even if the listener was called after the event

Terminology:
1. fulfilled - The action relating to the promise succeeded
2. rejected - The action relating to the promise failed
3. pending - Hasn't fulfilled or rejected yet
4. settled - Has fulfilled or rejected