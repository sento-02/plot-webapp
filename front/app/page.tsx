"use client"

import { PlotRequest } from './api/api'
import React, { useState, useEffect } from "react"
import { useRouter } from 'next/navigation'
import { InputCheckboxChild } from './components/checkbox'

type Fileinfo = {
    filename: string
    id: number
}

type Fileinfos = {
    list: Fileinfo[]
}

type Request = {
    id: string[]
    filename: string[]
    log: boolean
}

export default function Home(){

    // const [fileinfos, setFileinfos] = useState<Fileinfo[]>([])
    // useEffect(() => {
    //     const fetchFileinfo = async () => {
    //         const response = await fetch('/init')
    //         const data = await response.json() as Fileinfos
    //         setFileinfos(data.list)
    //     }
    //     fetchFileinfo()
    //   },[])


    // const router = useRouter()
    // const DisplayGraph = (hash:string, query:Request) => {
    //     router.push(`/${hash}`)
    // }


    // const [reqids, setReqids] = useState<string[]>([])
    // const handleIdChecked = (e: React.ChangeEvent<HTMLInputElement>) => {
    //     if (reqids.includes(e.target.value)) {
    //         setReqids(
    //         reqids.filter((checkedValue) => checkedValue !== e.target.value)
    //     );
    //     } else {
    //         setReqids([...reqids, e.target.value]);
    //     }
    // };

    // const [reqlog, setLog] = useState<boolean>(false)
    // const handleLogChecked = (chk: boolean) => {
    //     setLog(chk)
    // }

    // const [reqfilenames, setReqfilenames] = useState<string[]>([])
    
    // const plotGraph = async () => {
    //     const query:Request = {
    //         id: reqids,
    //         filename: reqfilenames,
    //         log: reqlog
    //     }
    //     const graphurl = await PlotRequest(query)
    //     DisplayGraph(graphurl, query)
    // }

    // const plotFromClick = async (data:Fileinfo) => {
    //     setReqids([data.id.toString()])
    //     setReqfilenames([data.filename])
    //     await plotGraph()
    // } 


    // const [checkedData, setCheckedData] = useState(false)
    // const handleChangeChecked = (chk: boolean) => {
    //     setCheckedData(chk)
    // }

    return (
    <main>
        {/* <div>
            <InputCheckboxChild
                value='log' 
                checked={reqlog}
                handleChange={(e) => handleLogChecked(e.target.checked)}
            />  
        </div>
        <div>
            <ul>
                {fileinfos.map(data => (
                <li key={data.id}>
                    <div onClick={() => plotFromClick(data)}>
                        {data.filename}
                    </div>
                    <div>
                        <InputCheckboxChild
                            value= {data.id.toString()}
                            checked={reqids.includes(data.id.toString())}
                            handleChange={handleIdChecked}
                        />
                    </div>
                </li>
                ))}
            </ul>
        </div>
        <button onClick={() => plotGraph()}>
            plot!
        </button> */}
        hello world!
    </main>
    )
}