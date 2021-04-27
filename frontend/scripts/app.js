
"use strict";
const modal = document.querySelector(".modal");
const overlay = document.querySelector(".overlay");
const btnCloseModal = document.querySelector(".close-modal");
const btnsOpenModal = document.querySelectorAll(".record");

const closeModal = function () {
  modal.classList.add("hidden");
  overlay.classList.add("hidden");
};

const openModal = function () {
  console.log("click me");
  modal.classList.remove("hidden");
  overlay.classList.remove("hidden");
};

for (let i = 0; i < btnsOpenModal.length; i++)
  btnsOpenModal[i].addEventListener("click", openModal);
btnCloseModal.addEventListener("click", closeModal);
overlay.addEventListener("click", closeModal);

document.addEventListener("keydown", function (e) {
  console.log(e.key);

  if (e.key === "Escape" && !modal.classList.contains("hidden")) {
    closeModal();
  }
});

const modal1 = document.querySelector(".modal1");
const btnCloseModal1 = document.querySelector(".close-modal1");
const btnsOpenModal1 = document.querySelectorAll(".btn1");

const closeModal1 = function () {
  modal1.classList.add("hidden1");
  overlay.classList.add("hidden1");
};

const openModal1 = function () {
  console.log("click me");
  modal1.classList.remove("hidden1");
  overlay.classList.remove("hidden1");
};

for (let i = 0; i < btnsOpenModal1.length; i++)
  btnsOpenModal1[i].addEventListener("click", openModal1);
btnCloseModal1.addEventListener("click", closeModal1);
overlay.addEventListener("click", closeModal1);

document.addEventListener("keydown", function (e) {
  console.log(e.key);

  if (e.key === "Escape" && !modal.classList.contains("hidden1")) {
    closeModal1();
  }
});

// overlay.addEventListener('click', function () {
//     modal.classList.add('hidden');
//     overlay.classList.add('hidden');
//   });

// for (let i = 0; i < btnsOpenModal.length; i++)
//   btnsOpenModal[i].addEventListener('click', function () {
//     console.log('click me');
//     modal.classList.remove('hidden');
//     overlay.classList.remove('hidden');
//   });



const addRows = function(response) {
    const records = response.data;
    const total = records.length;
    console.log(records[0])
    const headers = document.getElementById('home-second__tr-headers')
    let emptyCol = `
      <button class="home-second__btn">
        <img
          src="/img/8.svg"
          alt=""
          class="home-second__icon"
        />
      </button>
    `
    let editBtn = `
        <button class="home-second__btn btn1">
          <svg
            width="16"
            height="16"
            viewBox="0 0 16 16"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            class="home-second__icon"
          >
            <path
              d="M0 15.3664C0.4448 13.84 0.888 12.3136 1.3328 10.7872C1.368 10.6656 1.4048 10.544 1.4368 10.4224C1.488 10.2384 1.584 10.0896 1.7312 9.9664C1.8688 9.8528 1.9904 9.7168 2.1168 9.5904C4.2016 7.5248 6.2864 5.45921 8.3696 3.39201C8.4176 3.34401 8.4592 3.28961 8.4928 3.24801C8.776 3.53281 9.0416 3.80001 9.3376 4.09761C9.3056 4.12001 9.2432 4.15201 9.1952 4.20001C7.0352 6.35521 4.8768 8.5104 2.7216 10.6704C2.6448 10.7488 2.5808 10.856 2.5504 10.9616C2.2912 11.8176 2.0448 12.6784 1.7888 13.5376C1.7568 13.6448 1.7728 13.712 1.8544 13.7856C1.9872 13.9056 2.104 14.0432 2.2384 14.1616C2.2848 14.2016 2.3728 14.232 2.4288 14.2176C3.2896 13.9712 4.1488 13.72 5.0064 13.4608C5.08 13.4384 5.1488 13.376 5.2064 13.3168C7.3968 11.1328 9.584 8.9456 11.7712 6.76001C11.8128 6.71841 11.848 6.67201 11.872 6.64481C12.1824 6.9552 12.4832 7.256 12.8128 7.5856C12.7984 7.5952 12.7408 7.6192 12.7008 7.6592C10.544 9.7952 8.384 11.9264 6.2384 14.0736C5.9392 14.3744 5.6144 14.56 5.2128 14.6736C3.7888 15.0768 2.3712 15.5024 0.9504 15.92C0.856 15.9472 0.76 15.9728 0.6656 16H0.5376C0.4688 15.9696 0.3984 15.9424 0.3296 15.9104C0.1376 15.8208 0.072 15.6384 0 15.4608V15.3664ZM4.3024 12.7152C4.2608 12.4496 4.216 12.2064 4.1872 11.9632C4.1728 11.848 4.1264 11.8016 4.0144 11.7808C3.7408 11.728 3.4704 11.6592 3.2176 11.6032C5.4864 9.3296 7.7552 7.05441 10.0096 4.79361C10.3696 5.15361 10.7456 5.52801 11.1088 5.88961C8.8624 8.1424 6.5952 10.416 4.3024 12.7152ZM10.8368 1.02562C11.0416 0.825621 11.2464 0.612821 11.4656 0.414422C12.0944 -0.151977 12.9136 -0.139177 13.5264 0.459222C14.2032 1.11842 14.8704 1.78562 15.5296 2.46242C16.1536 3.10082 16.144 3.95521 15.5216 4.59201C15.3344 4.78401 15.1408 4.97121 14.9616 5.14721C13.592 3.77921 12.224 2.41282 10.8368 1.02562ZM9.168 2.53602C9.4784 2.24482 9.7968 1.94562 10.0992 1.66082C11.5328 3.09442 12.9584 4.52161 14.3968 5.96001C14.0976 6.24001 13.776 6.54241 13.4656 6.83361L9.168 2.53602Z"
              fill="#A0A4A8"
            />
          </svg>
        </button>
    `

    for(let i=0;i < total;i++) {
      let rowArriveTime = new Date(records[i].arrive_time);
      let rowExitTime = new Date(records[i].exit_time);
      let arrive_time = rowArriveTime.toLocaleString().split(', ')[1]
      let exit_time = rowExitTime.toLocaleString().split(', ')[1]
      let arrive_timeHours, exit_timeHours;

      arrive_timeHours = parseInt(arrive_time.slice(0,2));
      exit_timeHours = parseInt(exit_time.slice(0,2));

      let work_hours = Math.abs(arrive_timeHours - exit_timeHours)
      
      let newRecord = `
      <tr class="all">
        <td class="home-second__td home-second__td--first">
            <img src="./img/5.svg" alt="" class="home-second__img" />
            <p class="home-second__email">${records[i].email}</p>
        </td>
        <td class="home-second__td">${records[i].date}</td>
        <td class="home-second__td">${arrive_time}</td>
        <td class="home-second__td">${exit_time}</td>
        <td class="home-second__td">${work_hours}</td>
        <td class="home-second__td">${records[i].status === 0 ? 'NOT CHANGED' : 'CHANGED'}</td>
        <td class="home-second__td">No problem today</td>
        <td>
        ${i === total - 1 ? editBtn : emptyCol}
        </td>
      </tr>
      `
      headers.insertAdjacentHTML('afterend',newRecord)

    }
}
const token = 'fORoSETLqfhGWvRl4phVCkpeXLAC3z'

const createRecord = function() {
  const form = document.getElementById('home-form__create-record');
  const inputs = document.getElementsByTagName('input');
  const requestBody = {
      employee_id : 1,
      arrive_time : new Date(inputs[0].value).toISOString(),
      exit_time : new Date(inputs[1].value).toISOString(),
      date : inputs[2].value,
      status : 1
  }
  console.log(inputs[0].value)
  console.log(inputs[1].value)
  
  if(inputs[-1] !== "") {
    fetch('http://localhost:8000/absense_record/record_create/', { method: "post", headers: {
    'Content-Type': 'application/json;charset=utf-8','Authorization': 'Bearer ' + token
  },body: JSON.stringify({ employee_id : 1, date : inputs[2].value, end_date : null , comment: inputs[-1].value})}).then(response => console.log(response.json())).catch(e => console.log(e))
  }

  fetch('http://localhost:8000/record/record_create/', { method: "post", headers: {
    'Content-Type': 'application/json;charset=utf-8','Authorization': 'Bearer ' + token
  },body: JSON.stringify(requestBody)}).catch(e => console.log(e))
}

const requestBody = {
      employee_id : 1
}

const createBtn = document.getElementById('create-submit-btn');

createBtn.addEventListener('click', e => {
  createRecord();
})


const data = fetch('http://localhost:8000/employee_record/users_record/', { method: "post", headers: {
    'Content-Type': 'application/json;charset=utf-8'},body: JSON.stringify(requestBody)}).then(response => response.json()).then(data => addRows(data)).catch(e => console.log(e))