REACT

npm start
code in src/App.js

ELEMENTS

- what you want to appear on screen
- plain object desribing a component instance or DOM node and its desired properties
- contains only information about the component type, its properites and child elements
- immutable -> cant call any methods on it
- description object with two fields - [ type , props ]
- passed to ReactDOM.render(), will only rerender if properties have changed
- can represent 
	DOM TAGS   => const element = <div />;
	components => const element = <Welcome name="Sara" />;

PROPS

- Arguments passed to Components via HTML attributes
- const element = <Welcome name="Sara" />;
	props = {name: 'Sara}

COMPONENTS

- Building blocks of App  -> will have many
- Javascript class or fuction that optionally accepts inputs -> returns react element that describes section of UI
- const element = <Welcome name="Sara" />;
	represents the "Welcome" component
- funtion Welcome(props){
	return <h1> hello, {props.name} </h1>;
  } 

STATE

- similar to props except private and fully controlled by component
- use class with its own render method

class Clock extends React.Component {
  	render() {
    	return (
      	<div>
        	<h1>Hello, world!</h1>
        	<h2>It is {this.props.date.toLocaleTimeString()}.</h2>
      	</div>);}}

CONSTRUCTOR

-


JAVASCRIPT

- let, const -> equvalent to var
- class -> always uses constructor method (called whenever class is initialized)
	   uses strict -> variables cannot be used without being declared (var i = 0 vs i = 0)
- inheritance -> "extends"
	class Inherits extends Inheritsfrom {}
	"super" -> method refers to parent class
		   by calling super in constructor, we call parents constructor (gets access to parent properties and methods)
- arrow func: these are equivalent 
	x => x * 2 
	function(x) { return x * 2 }

JSX

ReactDOM.render(
  element,
  document.getElementById('root')
);

- Couples rendering logic with other UI logic
- wraps any valid js expressions in curly braces
	const name = 'Josh Perez';
	const element = <h1>Hello, {name}</h1>;
- can use JSX inside loops and if statements
  	if (user) {
  	  return <h1>Hello, {formatName(user)}!</h1>;
  	}
- automatically escapes user input