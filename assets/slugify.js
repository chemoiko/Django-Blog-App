//everytime there is a keyup event , its going to get that value from the title input and replicate in the slug input

const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

// Function to convert the title to a slug
const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')      // Replace & with '-and-'
        .replace(/[\s\W-]+/g, '-')   // Replace spaces, non-word characters and dashes with a single dash
        .replace(/^-+|-+$/g, '');    // Remove leading and trailing dashes
};

// Add an event listener to the title input to update the slug input on keyup
titleInput.addEventListener('keyup', (e) => {
    slugInput.value = slugify(titleInput.value);
});         //this listens to any key up events thats when u leave a pressed button