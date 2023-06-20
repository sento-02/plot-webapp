"use client"

import { PlotRequest } from './api/api'
import React, { useState, useEffect, ReactNode } from "react"
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
    log: boolean
}

export default function Home(){

    // get fileinfo from database
    const [fileinfos, setFileinfos] = useState<Fileinfo[]>([])
    useEffect(() => {
        const fetchFileinfo = async () => {
            const response = await fetch('/init')
            const data = await response.json() as Fileinfos
            setFileinfos(data.list)
        }
        fetchFileinfo()
      },[])

    //return graph endpoint
    const Graph = (hash:string, query:Request) => {
        return (
            <div>
                {hash ? <iframe src={"/"+hash} width="100%" height="600"></iframe> : <div> select data </div>}
            </div>
        )
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
    

    // handle log/liner
    const [reqlog, setLog] = useState<boolean>(false)
    const handleLogChecked = (chk: boolean) => {
        setLog(chk)
    }

    //handle graph endpoint
    const [Graphobject, setGraphobject] = useState<ReactNode>(null)
    const handleGraphobject = (graphurl: string, query: Request) => {
        const graph = Graph(graphurl, query)
        setGraphobject(graph)
    }

    //plot
    //need to modify: when PlotRequest returns null
    const plotGraph = async () => {
        const query:Request = {
            id: selectedIds.map(id => id.toString()), 
            log: reqlog
        }
        const graphurl = await PlotRequest(query)
        handleGraphobject(graphurl, query)
    }

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
        <Box>
            {Graphobject}
        </Box>
    </Layout>
    )
}