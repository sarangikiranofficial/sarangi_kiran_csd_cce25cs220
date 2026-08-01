function validateDressForm() {
    const name = document.getElementById('id_dress_name').value.trim();
    const size = document.getElementById('id_size').value.trim();
    const colour = document.getElementById('id_colour').value.trim();
    const price = document.getElementById('id_price').value.trim();
    const errorBox = document.getElementById('jsError');

    if (name === "" || size === "" || colour === "" || price === "") {
        errorBox.innerText = "Validation Error: No field should be left empty!";
        errorBox.style.display = "block";
        return false; 
    }

    errorBox.style.display = "none";
    return true;
}