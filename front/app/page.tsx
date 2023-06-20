"use client"

import { PlotRequest } from './api/api'
import React, { useState, useEffect } from "react"
import { useRouter } from 'next/navigation'
import { InputCheckboxChild } from './components/checkbox'
import Layout from './components/Layout'
import { DataGrid, GridRowSelectionModel } from '@mui/x-data-grid';
import { Box } from '@mui/material';
import Button from '@mui/material/Button';

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

    const [fileinfos, setFileinfos] = useState<Fileinfo[]>([])
    useEffect(() => {
        const fetchFileinfo = async () => {
            const response = await fetch('/test_file_list')
            const data = await response.json() as Fileinfos
            setFileinfos(data.list)
        }
        fetchFileinfo()
      },[])


    const router = useRouter()
    const DisplayGraph = (hash:string, query:Request) => {
        router.push(`/${hash}`)
    }


    const columns = [
        { field: 'id', headerName: 'ID', width: 70 },
        { field: 'filename', headerName: 'File Name', width: 200 },
      ];

    // handle selection
    const [selectedIds, setSelectedIds] = React.useState<(string | number)[]>([]);
    const handleRowSelectionChange = (rowSelectionModel: GridRowSelectionModel) => {
        setSelectedIds(rowSelectionModel as (string | number)[]);
      };
      


    const [reqids, setReqids] = useState<string[]>([])
    const handleIdChecked = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (reqids.includes(e.target.value)) {
            setReqids(
            reqids.filter((checkedValue) => checkedValue !== e.target.value)
        );
        } else {
            setReqids([...reqids, e.target.value]);
        }
    };

    const [reqlog, setLog] = useState<boolean>(false)
    const handleLogChecked = (chk: boolean) => {
        setLog(chk)
    }

    const [reqfilenames, setReqfilenames] = useState<string[]>([])
    
    const plotGraph = async () => {
        const query:Request = {
            id: selectedIds.map(id => id.toString()), 
            filename: reqfilenames,
            log: reqlog
        }
        const graphurl = await PlotRequest(query)
        DisplayGraph(graphurl, query)
    }
    

    const plotFromClick = async (data:Fileinfo) => {
        setReqids([data.id.toString()])
        setReqfilenames([data.filename])
        await plotGraph()
    } 


    // const [checkedData, setCheckedData] = useState(false)
    // const handleChangeChecked = (chk: boolean) => {
    //     setCheckedData(chk)
    // }

    return (
    <Layout>
        <Box> 
            <DataGrid 
            rows={fileinfos} 
            columns={columns} 
            checkboxSelection 
            onRowSelectionModelChange={handleRowSelectionChange} 
            rowSelectionModel={selectedIds}
            />
        </Box>
        <Box mt={1}>
            <Button variant='contained' onClick={() => plotGraph()}>
                Plot
            </Button>
        </Box>
    </Layout>
    )
}