$(() => {
    $('#calendar').calendar();
    eel.get_date_dictionary()()
        .then(dateDictionary => {
            $main = $('.main');
            $main.html(`<p>${JSON.stringify(dateDictionary)}</p>`);
        });
});