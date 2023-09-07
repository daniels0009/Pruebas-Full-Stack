/*Show menu*/
const navMenu = document.getElementById("nav-menu");
const navToggle = document.getElementById("nav-toggle");
const navClose = document.getElementById("nav-close");

if (navToggle) {
    navToggle.addEventListener("click", () => {
        navMenu.classList.add("show-menu");
    });
}
if (navClose) {
    navClose.addEventListener("click", () => {
        navMenu.classList.remove("show-menu");
    });
}

/*Remuve mobile menu*/
const navLink = document.querySelectorAll(".nav__link");

function linkAction() {
    const navMenu = document.getElementById("nav-menu")
    navMenu.classList.remove("show-menu")
}
navLink.forEach(n => n.addEventListener("click", linkAction));

/*Change background header*/
function scrollHeader() {
    const header = document.getElementById("header")
    if (this.scrollY >= 50) header.classList.add("scroll-header"); else header.classList.remove("scroll-header");
}
window.addEventListener("scroll", scrollHeader);

document.addEventListener("DOMContentLoaded", function () {
    // Función para mostrar el pop-up después de 2 minutos
    function showPopup() {
        setTimeout(function () {
            var popup = document.getElementById("popup");
            popup.style.display = "block";
        }, 120000); // 2 minutos en milisegundos
    }

    // Función para cerrar el pop-up
    document.getElementById("close-popup").addEventListener("click", function () {
        var popup = document.getElementById("popup");
        popup.style.display = "none";
    });
});

/*Testimonial swiper*/
let testimonialSwiper = new Swiper(".testimonial-swiper", {
    spaceBetween: 30,
    loop: "true",

    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});

/*New swiper*/
let newSwiper = new Swiper(".new-swiper", {
    spaceBetween: 24,
    loop: "true",

    breakpoints: {
        576: {
            slidesPerView: 2,
        },
        768: {
            slidesPerView: 3,
        },
        1024: {
            slidesPerView: 4,
        }
    }
});

/*Scroll sections active link*/
const sections = document.querySelectorAll("section[id]");

function scrollActive() {
    const scrollY = window.pageYOffset

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight,
            sectionTop = current.offsetTop - 58,
            sectionId = current.getAttribute("id");
        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            document.querySelector(".nav__menu a[href*=" + sectionId + "]").classList.add("active-link");
        } else {
            document.querySelector(".nav__menu a[href*=" + sectionId + "]").classList.remove("active-link");
        }
    });
}
window.addEventListener("scroll", scrollActive);

/*Show scroll up*/
function scrollUp() {
    const scrollUp = document.getElementById("scroll-up");
    if (this.scrollY >= 400) scrollUp.classList.add("show-scroll"); else scrollUp.classList.remove("show-scroll");
}
window.addEventListener("scroll", scrollUp);

/*Show cart*/
const showCart = document.getElementById("cart");
const cartShop = document.getElementById("cart-shop");
const cartClose = document.getElementById("cart-close");

if (cartShop) {
    cartShop.addEventListener("click", () => {
        showCart.classList.add("show-cart");
    });
}
if (cartClose) {
    cartClose.addEventListener("click", () => {
        showCart.classList.remove("show-cart");
    });
}


/*Display products*/
const productsEl = document.querySelector(".products__container");
const featuredEl = document.querySelector(".featured__container");
const newArrivalsEl = document.querySelector(".new__products__container");
const cartItemsEl = document.querySelector(".cart__container");
const totalPriceEl = document.querySelector(".cart__prices-total");
const totalItemsEl = document.querySelector(".cart__prices-item");
const totalItemsInCartEl = document.querySelector(".total-items-cart");

function renderProducts() {
    products.forEach((product) => {
        productsEl.innerHTML += `
            <article class="products__card">
                <img src="${product.img}" alt="" class="products__img">
                <h3 class="products__title">${product.title}</h3>
                <span class="products__price">${product.price}</span>
                <button class="products__button" onclick="addToCart(${product.id})">
                    <i class='bx bx-shopping-bag add-cart'></i>
                </button>
            </article>
        `;
    })
}
renderProducts();

function renderFeaturedProducts() {
    featured.forEach((featured) => {
        featuredEl.innerHTML += `
            <article class="featured__card">
                <span class="featured__tag">Sale</span>
                <img src="${featured.img}" alt="" class="featured__img">
                <div class="featured__data">
                    <h3 class="featured__title">${featured.title}</h3>
                    <span class="featured__price">${featured.price}</span>
                </div>
                <button class="button featured__button" onclick="addToCart(${featured.id})">ADD TO CART</button>
            </article>
        `;
    })
}
renderFeaturedProducts();

function renderArrivalProducts() {
    newArrivals.forEach((newArrivals) => {
        newArrivalsEl.innerHTML += `
            <article class="new__card swiper-slide">
                <span class="new__tag">New</span>
                <img src="${newArrivals.img}" alt="" class="new__img">
                <div class="new__data">
                    <h3 class="new__title">${newArrivals.title}</h3>
                    <span class="new__price">$${newArrivals.price}</span>
                </div>
                <button class="button new__button" onclick="addToCart(${newArrivals.id})">ADD TO CART</button>
            </article>
        `;
    })
}
renderArrivalProducts();

/*Cart functions*/
let cart = JSON.parse(localStorage.getItem("CART")) || [];
updateCart();

function addToCart(id) {

    if (cart.some((item) => item.id === id)) {
        changeNumberOfUnits("plus", id)
    } else {
        const item = products.find((product) => product.id === id)
        const featItem = featured.find((feat) => feat.id === id)
        const newItem = newArrivals.find((newArr) => newArr.id === id)
        const homeItem = home.find((homeProd) => homeProd.id === id)
        cart.push({
            ...item, ...featItem, ...newItem, ...homeItem,
            numberOfUnits: 1,
        });
    }
    updateCart();
}

function updateCart() {
    renderCartItems();
    renderSubtotal();

    localStorage.setItem("CART", JSON.stringify(cart));
}

function renderSubtotal() {
    let totalPrice = 0, totalItems = 0;
    cart.forEach((item) => {
        totalPrice += item.price * item.numberOfUnits;
        totalItems += item.numberOfUnits;
    })

    totalPriceEl.innerHTML = `$ ${totalPrice.toFixed(2)}`;
    totalItemsEl.innerHTML = `${totalItems}`;
    totalItemsInCartEl.innerHTML = totalItems;
}

function renderCartItems() {
    cartItemsEl.innerHTML = "";
    cart.forEach((item) => {
        cartItemsEl.innerHTML += `
        <article class="cart__card">
        <div class="cart__box">
            <img src="${item.img}" alt="" class="cart__img">
        </div>
        <div class="cart__details">
            <h3 class="cart__title">${item.title}</h3>
            <span class="cart__price">${item.price}</span>
            <div class="cart__amount">
                <div class="cart__amount-content">
                    <span class="cart__amount-box" onclick="changeNumberOfUnits('minus', ${item.id})">
                        <i class='bx bx-minus'></i>
                    </span>
                    <span class="cart__amount-number">${item.numberOfUnits}</span>
                    <span class="cart__amount-box" onclick="changeNumberOfUnits('plus', ${item.id})">
                        <i class='bx bx-plus'></i>
                    </span>
                </div>
                <i class="bx bx-trash-alt cart__amount-trash" onclick="removeItemFromCart(${item.id})"></i>
            </div>
        </div>
        </article>
        `;
    })
}

function removeItemFromCart(id) {
    cart = cart.filter((item) => item.id !== id);

    updateCart();
}

function changeNumberOfUnits(action, id) {
    cart = cart.map((item) => {
        let numberOfUnits = item.numberOfUnits;
        if (item.id === id) {
            if (action === "minus" && numberOfUnits > 1) {
                numberOfUnits--;
            } else if (action === "plus" && numberOfUnits < item.instock) {
                numberOfUnits++;
            }
        }
        return {
            ...item,
            numberOfUnits,
        };
    })

    updateCart();
}