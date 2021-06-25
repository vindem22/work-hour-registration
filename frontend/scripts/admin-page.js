let userName;
let user;

function personalData(data) {
  const pageName = document.querySelector('.sidebar__user-name');
  user = data.email;
  console.log(pageName)
  pageName.textContent = data.first_name + " " + data.last_name;
}

fetch('http://localhost:8000/employee/1/').then(response => response.json()).then(data => personalData(data))


function addRecords(response) {
    console.log(response)
    const records = response.data;
    const headers = document.getElementById('table__headers')
    const total = response.total;

    for(let i = 0;i < total;i++) {
        let newRecord = `
        <tr class="table__row">
            <td class="table__col-user"><a href='AdminReports.html?id=${records[i].id}'>${records[i].email}</a></td>
            <td class="table__col-firstname">${records[i].first_name}</td>
            <td class="table__col-lastname">${records[i].last_name}</td>
            <td class="table__col-worked-hours">${records[i].work_hours}</td>
            <td class="table__col-flex-status">${records[i].flex_status}</td>
            <td class="table__col-records">${records[i].records_count}</td>
            <td class="table__col-reports-num">${records[i].reports_count}</td>
            <td class="table__col-edit-btn">Edit</td>
        </tr>
        `
        headers.insertAdjacentHTML('afterend',newRecord)
    }
}


const data = fetch('http://localhost:8000/employee/').then(response => response.json()).then(data => addRecords(data.data)).catch(e => console.log(e))




