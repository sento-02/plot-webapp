import { request } from "http"

type Request = {
    id: string[]
    filename: string[]
    log: boolean
}

type URLresponse = {
    url: string
}

export const PlotRequest = async (req:Request) => {
    const response = await fetch('/test/graph', {
        method: 'POST',
        headers: {'Content-Type': 'application/json',},
        body: JSON.stringify(req),
    })
    const data = await response.json() as URLresponse
    return data.url
}