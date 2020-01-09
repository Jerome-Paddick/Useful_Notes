Vue

===

React uses functional programming paradimes (always use immutable data structures), Vue does not

BASICS

CLI - Command Line Interface
npm install -g @vue/cli

---
### Templates

- Vue equivalent to JSX
- Tells Vue where to look in the DOM when it want to make changes
- Accompanied with js file that will house Vue code

#### Directives

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

#### GLOBAL SCOPE  
    
- Available Anywhere in the application


    Vue.prototype.$globalValue = 'Global Scope!';


#### Sub-tree scope

- Scoped to a specific part of the application  
- best used to share contextual information

#### Component scope

- 

#### Instance scope

The $ sign is used in Vue.js to identify properties that can be used in all available instances in any given Vue project

---
### DATA

    GETTERS

- for each instance variable, a getter returns its value


    SETTER
    
- For each instance variable, a setter method sets or update its value

---
### Typescript

- Superset of Js
- statically compiled to pure js
- can be run in node js and most browsers
- uses types and interfaces to describe data
- uses generics -> functions where types can be specified later
- prototyping -> behavour reuse through inherritence 


      <div>
        <b-alert show>[{{user}}]</b-alert>
      </div>
      <div>
        <b-alert show>[{{settings}}]</b-alert>
      </div>

      <div class="ui container">
        <div class="section-header shadow" @click="visibleIndex = (visibleIndex == 5 ? -1 : 5)">
          <span class='title'>ASDF</span>
        </div>
        <div class='section-body' v-if="visibleIndex == 5">
          <table>
            <trhead>
              <th>ASDF</th>
            </trhead>
            <tr v-for="(z, index) in settings.User" :key="index">
            <td>{{index}}</td>
            <td>{{z.firstName}}</td>
            </tr>
          </table>
        </div>
      </div>