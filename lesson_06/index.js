let count = 0

function updateCount(e) {
    count++; // update the counter

    console.log('Updating count to', count)
    document.querySelector('#count_input').value = count; // update the element
}