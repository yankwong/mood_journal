
$(() => {
    $('#calendar').calendar({
        maxYear: 1
    });

    eel.get_date_dictionary()()
        .then(dateDictionary => {
            $main = $('.main');

            for (const date in dateDictionary) {
                const [month, day, year] = date.split('/');
                $calendarItem = $(`.jqyc-day-${day}.jqyc-day-of-${month}-month`).addClass('tweeted');
            }
        });
});