# Actions with Javascript

The way to make anything happen other than just css movement or a form submit is to use Javascript.

## Steps

### HTML page
Start with a new html page
```html
<!DOCTYPE html>
<html lang="en">

<head>
	<title>JavaScript</title>
</head>

<body>
	<div>
		<input id="alert_text" placeholder="Alert text" />
		<button id="alert_button">Alert</button>
	</div>
</body>

</html>
```

If you open your page you should see an input and a button. The first goal will be to have an alert pop up when you click the button.

### Inline Javascript

Like CSS you can add the code into the html itself or into another file. If you want to add it into the html you add a tag called `<script>`

Our script is going to look for an element as soon as it gets loaded so we will need at at the bottom of our file. Right before the `</div>` add this.
```html
<script>
    const alertButton = document.querySelector('#alert_button');
    alertButton.onclick = (e) => {
        const text = document.querySelector('#alert_text').value || 'Nothing to alert';
        console.log("Going to alert", text)
        alert(text);
    }
</script>
```



This is dong a lot. Let's go line by line

```javascript
const alertButton = document.querySelector('#alert_button');
```
 `const` says to make a new variable that we can use later, we are naming it `alertButton`. The `=` tell what that variable will hold. `document` is a special variable built into web pages to interact with the page. The `.` looks for a function on the variable. [`querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) is a function built into the document that gets an element. `()` tells javascript to run a function with whatever is inside the `()`s as `arguments` to the function. In our case we are using `#alert_button` which similarly to our `css` files says find an element that has an `id=alert_button`.

```javascript
alertButton.onclick = (e) => {    }
```
[`onclick`](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event) is a special function on elements that gets called when you click on them. There are a few ways to make a function but  we are using the compact way of [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) using `=>`. They are formed `(arguments) => { what heppens inside the fuction}`. Onclick send the argument of an element when clicked on that is the `(e)` so we can do things to the element we clicked on.


```javascript
const text = document.querySelector('#alert_text').value || 'Nothing to alert';
```
This is making a variable `text` by looking up the `value` of the input with `id=alert_text`. If that value is empty the `||`, aka OR, fills in other text so we don't open a blank alert.

```javascript
console.log("Going to alert", text)
```
`console.log` is another special function that prints text to the `console`. Find that by right clicking on the page and clicking `Inspect`. This will print the text inside the `""` and whatever your variable `text` is set to.

```javascript
alert(text);
```
`alert` is shorthand for [`window.alert`](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert). It is another function included in all browser to pop up an alert message. We are sending our `text` variable to it.

Try your button!

### External File

Crate a new file called `index.js`. `js` is the file extension for javascript. Then add a html `<script>` tag so the page gets included by your html file. This time in your `head` add this
```html
<script src="./index.js"></script>
```
Lets add a new elements for this new script after the other </div>

```html
<div>
    <button id="count_button" onclick="(e) => updateCount(e)">Counter</button>
    Count <input id="count_input" value="0" disabled />
</div>
```
In this case instead of finding the button by `document.querySelector` we are just adding the `onclick` right into our html. `onclick="updateCount()"` Tells the html to look for a javascript function called `updateCount()` when it is clicked on.


Put this inside your `.js` file
```javascript
let count = 0

function updateCount() {
    count++; // update the counter
    console.log('Updating count to', count)
    document.querySelector('#count_input').value = count; // update the element
}
```
Let's go over lines again
```javascript
let count = 0
```
`let` like `const` crates a variable but you can change the value later. We put that outside the function so the current value is saved into memory.

```javascript
function updateCount() { }
```
This is like our arrow function `=>` but the longer from of the keyword `function` followed by a name so it can be called by our html.

```javascript
count++;
```
`++` is short hand for `count = count + 1` This adds one to the count variable every time the function is called.

```javascript
document.querySelector('#count_input').value = count;
```
We are using `document.querySelector` to find an element with `id=count_input`. Then setting its value to our `count` varible. This will update the page.

Save and try it out!
