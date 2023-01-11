import {useEffect} from "react";
import {api} from "./consts";

export function useMakeGetRequest(setState, dataPreparing, send) {
    useEffect(() => {fetch(`${api}/api/wishes`, {method: 'GET', headers: {'Accept': 'application/json',}}).then(response => {
            if (response.status === 200 || response.status === 201) {
                return response;
            }
            throw new Error();
        }).then(response => response.json()).then(data => {setState(dataPreparing(data))});
    }, [send])
}