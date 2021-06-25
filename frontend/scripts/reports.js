const CLIENT_ID = 'QS1lmDYxbmIeVSbZFW22HPweyL2lFzX9qCrBfRMW'
const CLIENT_SECRET = 'TpI1AE4e8SJusMmTKojgl8cPDMivbBZCLUcmiTWun76mV2gzW39ucXxMcsHwek4Ar55Ydzsqs3DiV5ZmHY3oABdd9PSbgqjYynq8hsXTmLy2argiM0QXPXGiVLVWqWX6'
const addRows = function(response) {
    const records = response.data;
    const total = records.length;
    console.log(response)
    const headers = document.getElementById('table__headers')
    let emptyCol = `
      <button class="home-second__btn">
        <img
          src="/img/8.svg"
          alt=""
          class="home-second__icon"
        />
      </button>
    `

    for(let i=0;i < total;i++) {
      let rowDateTime = new Date(records[i].date);
      let date_time = rowDateTime.toLocaleString().split(', ')[1]


      let newRecord = `
        <tr class="all">
          <td class="home-second__td home-second__td--first">
              <p class="home-second__email">${records[i].employee_id}</p>
          </td>
          <td class="home-second__td">${records[i].comment === "" ? "No comments" : records[i].comment}</td>
          <td class="home-second__td">${date_time}</td>
          <td class="home-second__td">${records[i].end_date}</td>
          <td>
          ${emptyCol}
          </td>
        </tr>
      `
      headers.insertAdjacentHTML('afterend',newRecord)

    }
}

const urlParams = new URLSearchParams(window.location.search);
const queryId = urlParams.get('id');


const data = fetch('http://localhost:8000/employee_record/users_absense_record/', { method: "post", headers: {
    'Content-Type': 'application/json;charset=utf-8'},body: JSON.stringify({employee_id : parseInt(queryId)})}).then(response => response.json()).then(data => addRows(data)).catch(e => console.log(e))