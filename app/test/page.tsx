"use client"

import { useState, useEffect } from "react"

type Data = {
    filename: string
    id: number
}

type Datas = {
    list: Data[]
}

export default function Home(){
    const [datas, setData] = useState<Data[]>([])
    useEffect(() => {
        const fetchData = async () => {
            const response = await fetch('test/file_list')
            const data = await response.json() as Datas
            setData(data.list)
        }
        fetchData()
      },[])

    
    return (
        <div>
      <ul>
        {datas.map(data => (
          <li key={data.id}>{data.filename}</li>
        ))}
      </ul>
    </div>
    )
}