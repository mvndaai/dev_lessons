# Form

We are going to make an `html` page that includes a form with submit.

## Steps

### Frame

Start by creating a file call `index.html` in a folder called `form`.

Note: We call it `index` because when you do not include a filename and just include a folder in a website it default looking for `index.html`.

```html
<!DOCTYPE html>
<html lang="en">

    <head>
    </head>

    <body>
    </body>
</html>
```

I like to think of HTML as blocks that you stack on top of each other. They all start with `<type>` and end with `<type/>` where `type` is the specific type of element. This say there is an `html` element that holds a `head` and `body`. `DOCTYPE` is a special tag that is required.

### Head
`head` doesen't change the look of the webpage itself, but it holds all the information needed to load the page and change other things in the browser. We are adding a `title` which will change what the browser tab is named

```html
<head>
    <title>Form</title>
</head>
```

Click `Go Live` in vscode to open the page. After each new addition refresh the page to see the changes.

### Header

There are different tags that contain text. `p` is for paragraph and there are different sizes of headers for different sections of the page `h1` is the biggest then you can do `h2`, `h3`, and so on. Add a `h1` to your body.

```html
<body>
    <h1>Form</h1>
</body>
```

### Form container

`form` is a special element that holds inputs that people can interact with like places to type and buttons.

```html
<body>
    ...
    <form action="./submit.html">
    </form>
</body>
```

Within tags you can specify attributes like the `action`. Different types of tags have different attributes with that you specify with an `=`. In this case `action` says when you submit this form it will go to a related page `./submit.html`

### Submit button

Let's stop for a moment and make a new page called `submit.html` that will open when we click our new input. It doesn't matter what is in the file. You can copy the submit in this package or leave it empty.

Now add a new `input` element with the attribute `type=submit` within your `form`. Inputs do not allow anything inside of them so they close themselves by ending with `/>`.

```html
<form ...>
    <input type="submit" />
</form>
```

### Text input

Add this before your submit button
```html
<div>
    <label>Name:
        <input type="text" name="text" id="text" placeholder="name" required />
    </label>
</div>
```

There is a lot to talk about.

Elements:
* `div` is an element that is used for spacing things out. Use them so everything does not go together on one line.
* `label` tell that the text inside it is related to an input. It helps e-readers for blind people interact with the website even if they can't see it
* `input` like the submit before is something a user can interact with

Attributes:
* `type` tells what kind of [type](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input) the input can do.
* `name` is a special attribute in a form that is used as a key for the value within the input
* `id` let you specify a unique way to programatically interact with a object, like making it pretty or automation.
* `placeholder` shows text within the textbox to help people know what to type in.
* `required` stops a submit from working if it is emtpy.


### Number

After the text input add this
```html
<div>
    <label for="number">
        Number between 1 and 10:
    </label>
    <input type="number" name="number" id="number" min="1" max="10" value="5" />
</div>
```

In this example to show a different way you can use a `label` we put the `input` on the same level instead of inside. When you do that you need a `for` where the value needs to match the `name` of an input.

Our new input has a `type` of [number](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/number) that allows for attribute of `min` (minimum), `max` (maxium), and `value (default value when the page loads).

### Checkbox

[Checkboxes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox) allow selected multiple items in a list.

```html
<div class="c-group">
    Pet growing up:
    <label><input type="checkbox" name="checkbox" value="dog">Dog</label>
    <label><input type="checkbox "name="checkbox" value="cat">Cat</label>
    <label><input type="checkbox" name="checkbox" value="fish" checked>Fish</label>
</div>
```

This time we added a `class` which is like an `id` but resuable. `value` is what will get sent when clicked on. The `input` is the value shown. `checked` specifies it if is checked when the page loads.

### Radio

[Radio](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/radio) buttons let someone choose one options amoung many. For the selection to work they all need to have the same `name`.


```html
<div>
    Summer is the best season:
    <label><input id="radio_true" type="radio" value="true" name="radio" checked /> True</label>
    <label><input id="radio_false" type="radio" value="false" name="radio" /> False</label>
</div>
```

### Select

When there are too many options for a radio button to work you can instead use [`select` with `option`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select).

```html
<div>
    <label for="select">
        Select a Nato phonetic Letter:
    </label>
    <select id="select" name="select">
        <option value="None" selected disabled>Select a letter</option>
        <option value="A">Alpha</option>
        <option value="B">Bravo</option>
        <option value="C">Charlie</option>
    </select>
</div>
```

This creates a `select` element that holds `option` elements. This uses new attributes of `selected` or `disabled`. `selected` is similar to `checked` to specifiy a default when the page loads. `disabled` allows you to put text like a `placeholder` that is not selectable.

## Test and Play
You should now be able interact with your new page. Congratulations! Play with it. When you click the submit button the page you go to should have all the `names` and `values` in the URL. It will look similar to below. The `?` starts the "Query Parameters" and there is an `&` between each.
```
http://localhost:5050/submit.html?checkbox=dog&number=5
```


## Notes

* `localhost` in the URL is telling you that the website is hosted on your local computer.
* The `:5050` is a `port`. Computers have a lot of ports to let other computers connect to them. `80` is the default for `http` and `443` is the default for https. If a webpage does not have a port it is on either 80 or 443. You can use almost any port you want but people like to use ones like `5050`, `8080` and `8888` for development.
* Open Chrome Tools and go to `Lighthouse` to get hints on how to improve the page
