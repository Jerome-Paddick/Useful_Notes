Typescript
===

#### Basics 
- Superset of Js
- statically compiled to pure js
- can be run in node js and most browsers
- uses types and interfaces to describe data
- uses generics -> functions where types can be specified later
- prototyping -> behavour reuse through inherritence 


    protected

Protected methods are `only` accessible from inside the class and extending class

Private methods are `only` accessible from inside the class

    interface

- Defines the specifications for an entity
- Contains the names and types of the properties


    interface TeslaModelS {
    length: number;
    width: number;
    wheelbase: number;
    seatingCapacity: number;
    getTyrePressure: () => number;
    getRemCharging: () => number;
    }

use:

    function buildTeslaModelS (teslaObj: TeslaModelS) {}
    
if function called with a "teslaObj" with incorrect types, ts will throw error

    namespace
    
Defines 


    @namespace 
    
- 2 different modules will never contribute the same name to the same scope
- Provides local grouping of constructs to prevent collisions


    async await
    
asyncronously wats for promised input

    const startAsync = async callback => {
      await wait(1000);
      callback('Hello');
      await wait(1000);
      callback('And Welcome');
      await wait(1000);
      callback('To Async Await Using TypeScript');
    };

---
#### Vuex

State management pattern + library for Vue.js

Centralised store for components in an application with rules for predictable mutations

`Store` - container that holds application state

- Stores are Reactive - vue components will be updated if stores change
- Store state cannot be directly mutated - can only be changed by explicitly `commiting mutations`  
--> state changes leave trackable record

- needs: Initial State Object & Mutations 


    const store = new Vuex.Store({
    state: {
    count: 0
    },
    mutations: {
    increment (state) {
      state.count++
    }}})
        
        
Access State

        store.state
        
        console.log(store.state.count)
        
Trigger state change

        store.commit()
        
        store.commit('increment')
        

        
        


- ctp2 calls Vue.use(Vuex); in `store.index.ts`

---
#### Local Storage

    json formatted storage in local browser
    
- Storage much larger than cookies (5Mb)
- Information never transmitted to the server -> only client side
- Per Origin (per domain and protocol)
- All pages from one origin can store anc access data


    window.localStorage
    
    localStorage.getItem()
    localStorage.setItem()
    localStorage.removeItem()
    localStorage.clear()
    
for storage which expires on tab close -> `window.sessionStorage`

---

#### Mutations

Only way to change a state in a Vuex store is by committing a mutation

---

    <div id="demo">
      <button @click="show1 = !show1">
        Toggle
      </button>
    
      <transition name="slide">
        <div v-if="show" class="overlay">
            <form class="ui small form" @submit.prevent="handleSubmit" autocomplete="off">
                <div>
                  Name
                </div>
                <input type="text" placeholder="Enter first name" name="firstname">>
              <div class="close">
                      <button type="submit">
                        Accept
                      </button>
                <i @click="show = !show" class="fas fa-times"></i>
              </div>
            </form>
          </div>
      </transition>
    
      </div>
