import './App.css';
import {useState} from "react";
import {api} from "./consts";
import {useMakeGetRequest} from "./useMakeRequest";
import pck from '../package.json'


function App() {
    const makePostRequest = (query, isSend, sending) => {
        return fetch(`${api}/api/wish?title=${query.title}&author=${query.author}&description=${query.description}&whom=${query.whom}`, {
            method: 'POST',
            headers: {'Accept': 'application/json',}
        }).then(response => {
            if (response.status === 200 || response.status === 201) {
                isSend(!sending)
                return response;
            }
            throw new Error();
        });
    }
    const addApiInfo = (data) => {
        setApiVersion(data["api_info"]["version"]);
        setReplica(data["api_info"]["replica_id"]);
    }

    const dataPreparing = (data) => {
        let wishes = data["wishes"];
        let arr = []
        addApiInfo(data);
        for (let wish of wishes) {
            arr.push(
            <div className="wishBlock">
                <div>{`Название : ${wish["title"]}` }</div>
                <div className="wishDescription">{`Описание : ${wish["description"]}`}</div>
                <div>{`Автор : ${wish["author"]}`}</div>
                <div>{`Кому : ${wish["whom"]}`}</div>
            </div>
            )
        }
        return arr
    }

    const [apiVersion, setApiVersion] = useState('0')
    const [replica, setReplica] = useState('0')
    const [state, setState] = useState([])
    const [sending, isSend] = useState(false)
    const [data, setData] = useState({  "wish_id": "",
        "author": "",
        "description":"" ,
        "title": "",
        "whom": ""})
    useMakeGetRequest(setState, dataPreparing, sending);
    return (
      <div className="main">
          <div className="apiInfo"></div>
          <div>{`Версия api: ${apiVersion}`}</div>
          <div>{`Версия web: ${pck.version}`}</div>
          <div>{`Реплика: ${replica}`}</div>
          <h1 className="appName">Сервис желаний</h1>
          <form className="usersForm" onSubmit={(evt) => {
              evt.preventDefault();
              makePostRequest(data, isSend, sending);}
          }>
              <label>
                  Название
                  <input className="title"  onChange={(evt) => {setData({...data, title: evt.target.value})}} placeholder="Введите название"/>
              </label>
              <label>
                  Описание
                  <input className="description" onChange={(evt) => {setData({...data, description: evt.target.value})}} placeholder="Введите описание"/>
              </label>
              <label>
                  Автор
                  <input className="author" onChange={(evt) => {setData({...data, author: evt.target.value})}} placeholder="Введите автора"/>
              </label>
              <label>
                  Кому
                  <input className="whom"  onChange={(evt) => {setData({...data, whom: evt.target.value})}} placeholder="Введите получателя"/>
              </label>
              <input type="submit" className="addWish"/>
          </form>
          <div className="wish">
              {state.map(x => x)}
          </div>
      </div>
  );
}

export default App;
