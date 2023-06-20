import { request } from "http"

type Request = {
    id: string[]
    log: boolean
}

type URLresponse = {
    url: string
}

export const PlotRequest = async (req:Request) => {
    const response = await fetch('/graph', {
        method: 'POST',
        headers: {'Content-Type': 'application/json',},
        body: JSON.stringify(req),
    })
    const data = await response.json() as URLresponse
    console.log(data)
    return data.url
}