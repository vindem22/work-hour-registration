function addRecord([user, firstname, lastname, worked_hours, flex_status, records_manually, reports_number]) {
    const headers = document.getElementById('table__headers')
    let newRecord = `
    <tr class="table__row">
        <td class="table__col-user">${user}</td>
        <td class="table__col-firstname">${firstname}</td>
        <td class="table__col-lastname">${lastname}</td>
        <td class="table__col-worked-hours">${worked_hours}</td>
        <td class="table__col-flex-status">${flex_status}</td>
        <td class="table__col-records">${records_manually}</td>
        <td class="table__col-reports-num">${reports_number}</td>
        <td class="table__col-edit-btn">Edit</td>
    </tr>
    `
    headers.insertAdjacentHTML('afterend',newRecord)
    console.log(newRecord)
}

const data = fetch('http://localhost/employee/').then(response => response.json()).then(data => console.log(data)).catch(e => console.log(e))

for(let i = 0; i < 10;i++) {addRecord(['bekmaganbetov@magil.ru', 'Zhanbolat', 'Bekmaganbetov', '45', '3', '43', '31']);}


