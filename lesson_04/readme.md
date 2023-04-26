# Make things pretty with CSS

This lesson we will use CSS, Cascaded Style Sheets, to style a webpage.

## Steps

### Create a new html file.

Create a file with this as a base

```html
<!DOCTYPE html>
<html lang="en">

<head>
	<title>Pretty</title>
</head>

<body>
	<h1>Prettier with Style</h1>
    <div class="border">
        <div class="column">
            <div class="row">
                <div id="a" class="box red">A</div>
                <div id="b" class="box blue">B</div>
            </div>
            <div class="row">
                <div id="c" class="box blue">C</div>
                <div id="d" class="box red">D</div>
            </div>
        </div>
    </div>
    <div id="catch">Hover here</div>
</body>

</html>
```

As you can see in our body there is a header, then lots of divs in different spaces.

Click `Go Live` in vscode to load the website and see what it looks like.

## Inline style

Styling usually goes in the `head` of your html files. Add this to start styling your page.

```html
<style>
    body, .column {
        background-color: linen;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .row {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }
</style>
```

To explain what all that does:

The part before `{}` is how the elements are referenced in the document. `body` is the body. The `.` means class. So these are looking for the classes of `row` and `column`. If you want to sytle two things the same way you put a `,` between them.

The parts inside `{}` are what stype is getting applied to the elements. `background-color` changes the background color. Choose whatever color you want. There are some default names or you can use [rgb or hex](https://htmlcolorcodes.com/).

I like using [flexboxes](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) to style a page. It makes sections easily grow and strink to fit different web pages and centers easily. `display: flex` is how we say we are using a flexbox. `flex-direction` lets you choose between `column`, up and down, or `row`, left and right. `justify-content: center` and `align-items: center` are just ways to make sure everything is centered.

Refesh the page and look what changed.

### Style file

Create a new file called `pretty.css` so we can put all our styles into a new file. Then add this line to your html `head` to make your html file use that file.

```html
<link rel="stylesheet" href="./pretty.css"/>
```

The `./` means you are finding a file in the same folder as the html file. If you want to go to another file start with `/` as the root and fillow from there. `../` will go up one folder if wanted.


### Colors

Add a new section to your `.css` file
```css
.red {
    background-color: red;
    color: white;
}
```

This changes anything with the class red to have a different `background-color` and font `color`.

Then add
```css
.red:active {
    background-color: pink;
    color: black;
}
```

Anything after a `:` does something special in css. `:active` only apply the style when element is clicked on. This will change the color when you click on it.

Lets finish by also adding colors for the blue class

```css
.blue {
    background-color: lightblue;
}
.blue:active {
    background-color: darkblue;
    color: white;
}
```

### Boarder

A boarder to an element
```css
.border {
    border: 4px solid green;
    padding: 10px;
}
```
This will make a border that is 4 pixels wide solid and green. You can cange the size or style of the boarder. Try `dotted` instead of `solid`.

To space out an element use `padding` and `margin`. Padding adds space on the inside and margin adds space on the outside.



Another special action like `:active` is `:hover` which only changes the style when a mouse is hovering over an item. To change the color when hovering add this.
```css
.border:hover {
    border-color: purple;
}
```

### Spacing and more

Add one more section to make each of the letters look better.
```css
.box {
    margin: 2px;
    padding: 2px 6px 2px 6px;
    font-size: 24px;

    border-radius: 10px; /* Round edges */
    cursor: pointer;
    user-select: none;
}
```

`margin` is adding space between each element.

`padding` is spacing the inside. You can use the different keys `padding-top`, `padding-bottom`,`padding-left`, and `padding-right` or just use the shorthand `padding`. If you have 1 size it will do all sides. If you have 2 it will do top/bottom then left/right, or you can add 4 values to do all at once.

`font-size` will make it letters larger.

`border-radius` changes how round the borders are.

`cursor:pointer` will change the look of your mouse when you hover over it.

`user-select:none` makes it so you cannot highlight the text.

### Animation

You can animate css by using [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/transition). Lets add some code to make a small animation

```css
#catch {
    margin-top: 40px;
    position: relative;
    top: 0;
    transition: top ease 0.5s;
}
#catch:hover {
    top: -10px;
}
```

The `#` matches `id` like `.` matches class. So this will only change the element with an `id=catch` in the html.

`position:relative` and `top:0` say to make the element relative to the parent with the top of the parent. Our `hover` here will move the element up 10 pixels.
