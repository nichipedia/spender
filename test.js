// fetch('https://cors-anywhere.herokuapp.com/https://www.walmart.com/browse/womens-clothing', {
//     headers: {
//         'User-Agent': 'Mozilla/5.0', 
//         "content-type": "text", 
//         'Origin': 'null'
//     }
// })
// .then(res => res.text())
// .then(data => {
//     let nodes = $.parseHTML(data);
//     console.log(nodes);
// })
// .catch(err => {
//     console.error(err)
// });

$.ajax('https://cors-anywhere.herokuapp.com/https://www.walmart.com/browse/womens-clothing', {
    headers: {
        'User-Agent': 'Mozilla/5.0', 
        'Origin': '*',
        'content-type': 'text',
        'Host': 'Me'
    },
    success: (data, status) => {
        console.log(data);
    },
    error: (meh, status, err) => {
        console.error(`${status} : ${err}`);
    }
})