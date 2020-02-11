Vue

===

React uses functional programming paradimes (always use immutable data structures), Vue does not

BASICS

CLI - Command Line Interface
npm install -g @vue/cli
---
### Instances

- Every Vue application starts with a Vue instance
- We pass this instance an [options](https://vuejs.org/v2/api/#Options-Data) object


    var vm = new Vue({
      // options
    })
    
A Vue application consists of a root Vue instance (generally organised into a tree of nested components)

---
### MVVM

    Model-View-View-Model
    
---
### API

    Axios

Promise Based HTTP requests in browser and Node.js

- build in CSRF protection
- can abort requests
- supports upload progress
- API calls must enable CORS to be accessed inside the browser

Requests start from `axios` object

    axios({
      url: 'https://dog.ceo/api/breeds/list/all',
      method: 'get'
    })
---

### Modules

Modules have:
1. `dependencies` -> 
    - required for function of module
2. `exports` -> 
    - functions/vars/classes that are exposed publicly to anything that imports module
    - hard to import complete module by design  
    - exports can be named or defualt

Named exports

    export function function-name(x)
    -> import {function-name} from mymodule

    
Default exports

    export default function(x)
    -> import new-function-name from mymodule

Protected:


--- 

### Components

- Named Reusable Vue instances (accept same options objects)
- On creation, adds all properties found in its data object to Vue's `reactivity system`
- When data objects value changes, Vue will update the DOM repectivly


    export default {...}
    
- exports a single class or function
- so it can be used as a dependency
- create local registration for Vue component
    
      class ChildClass extends ParentClass { ... }
    
child inherits all methods from parent




---
### Templates

- Vue equivalent to JSX
- Tells Vue where to look in the DOM when it want to make changes
- Accompanied with js file that will house Vue code

#### - Directives

- Custom Vue attribute inserted into HTML element
- structured `'v-keyword'`
- eg. Conditional Rendering
    - renders if evaluation is truthy 


    <div @click="visibleIndex = (visibleIndex == 5 ? -1 : 5)">
    <div class='section-body' v-if="visibleIndex == 1">
or

    <ul>
      <li v-for=’name in listOfNames’>
      </li>
    </ul>

#### Cirly Braces

    {{ moustache }}
    
value of moustache will be replaced with the value of the corresponding data object

---
### Scope

4 unique levels of scope

GLOBAL SCOPE    
- Available Anywhere in the application

    Vue.prototype.$globalValue = 'Global Scope!';


SUB TREE SCOPE
- Scoped to a specific part of the application  
- best used to share contextual information

COMPONENT SCOPE

- 
INSTANCE SCOPE

The $ sign is used in Vue.js to identify properties that can be used in all available instances in any given Vue project

---
### DATA

    GETTERS

- for each instance variable, a getter returns its value


    SETTER
    
- For each instance variable, a setter method sets or update its value

---
### Decorators

[Vue Property Decorators](https://www.npmjs.com/package/vue-property-decorator)

- @Prop
- @PropSync
- @Model
- @Watch
- @Provide
- @Inject
- @ProvideReactive
- @InjectReactive
- @Emit
- @Ref
- @Component (provided by vue-class-component)

---
### Transitions

Vue provides a transition wrapper component, allowing you to add entering/leaving transitions for any element or component in the following contexts:

- Conditional rendering (using v-if)
- Conditional display (using v-show)
- Dynamic components
- Component root nodes

---

### New Form

1. 

---

