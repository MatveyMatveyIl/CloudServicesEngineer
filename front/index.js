const webVersion = "0.1.4"

const api = '';
function makeGetRequest() {
    return fetch(`${api}/api/wishes`, {
        method: 'GET',
        headers: {'Accept': 'application/json',}
    }).then(response => {
        if (response.status === 200 || response.status === 201) {
            return response;
        }
        throw new Error();
    });
}

function makePostRequest(query) {
    return fetch(`${api}/api/wish?title=${query.title}&author=${query.author}&description=${query.description}&whom=${query.whom}`, {
        method: 'POST',
        headers: {'Accept': 'application/json',}
    }).then(response => {
        if (response.status === 200 || response.status === 201) {
            location.reload();
            return response;
        }
        throw new Error();
    });
}

let apiInfoElement = document.querySelector(".apiInfo");
let wishElement = document.querySelector(".wish");
makeGetRequest().then(response => response.json()).then(data => dataPreparing(data));
let form = document.querySelector(".usersForm");
form.addEventListener("submit", (evt) => {
    evt.preventDefault();
    let requestData = {
        "wish_id": "",
        "author": document.querySelector(".author").value,
        "description": document.querySelector(".description").value,
        "title": document.querySelector(".title").value,
        "whom": document.querySelector(".whom").value
    };
    makePostRequest(requestData);
});

function addApiInfo(data) {
    let version = document.createElement("h");
    let replica = document.createElement("h");
    let webVersionEl = document.createElement("h");
    version.innerHTML = `Версия апи: ${data["api_info"]["version"]}`;
    replica.innerHTML = `Реплика: ${data["api_info"]["replica_id"]}`;
    webVersionEl.innerHTML = `Версия web: ${webVersion}`;
    apiInfoElement.appendChild(version);
    apiInfoElement.appendChild(replica);
    apiInfoElement.appendChild(webVersionEl);
}

function addStyleForWishBlock(wishBlock) {
    wishBlock.style.display = "flex";
    wishBlock.style.alignItems = "center";
    wishBlock.style.border = "black solid 1px";
    wishBlock.style.width = "290px";
    wishBlock.style.borderRadius = "5px";
    wishBlock.style.height = "114px";
    wishBlock.style.margin = "5px";
    wishBlock.style.flexDirection = "column";
    wishBlock.style.justifyContent = "space-between";
}

function addStyleForDescription(description) {
    description.style.display = "inline-flex";
    description.style.flexWrap = "wrap";
    description.style.overflowWrap = "break-word";
}

function dataPreparing(data) {
    let wishes = data["wishes"];
    addApiInfo(data);
    for (let wish of wishes) {
        let wishBlock = document.createElement("div");
        addStyleForWishBlock(wishBlock);
        let author = document.createElement("div");
        let description = document.createElement("div");
        let title = document.createElement("div");
        let whom = document.createElement("div");
        addStyleForDescription(description);
        description.innerHTML = `Описание : ${wish["description"]}`;
        whom.innerHTML = `Кому : ${wish["whom"]}`;
        title.innerHTML = `Название : ${wish["title"]}`;
        author.innerHTML = `Автор : ${wish["author"]}`;
        wishBlock.appendChild(title);
        wishBlock.appendChild(description);
        wishBlock.appendChild(author);
        wishBlock.appendChild(whom);
        wishElement.appendChild(wishBlock);
    }
}
