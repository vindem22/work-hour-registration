
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



const addRow = function() {
    const headers = document.getElementById('table__headers')
    let newRecord = `
    <tr class="all">
      <td class="home-second__td home-second__td--first">
          <img src="./img/5.svg" alt="" class="home-second__img" />
          <p class="home-second__email">dastanahmet@gmail.com</p>
      </td>
      <td class="home-second__td">10/10/2020</td>
      <td class="home-second__td">09:15</td>
      <td class="home-second__td">09:15</td>
      <td class="home-second__td">8 hours</td>
      <td class="home-second__td">NOT CHANGED</td>
      <td class="home-second__td">No problem today</td>

      <td>
          <button class="home-second__btn">
          <img
              src="/img/8.svg"
              alt=""
              class="home-second__icon"
          />
          </button>
      </td>
    </tr>
    `
    headers.insertAdjacentHTML('afterend',newRecord)
    console.log(newRecord)
}