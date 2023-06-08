"use client"

import { useRouter } from "next/navigation";

type MyRequest = {
   id: number[];
};

export default function Home(){
    const router = useRouter()
    return (
      <main>
        <div>
          <iframe src='/src/[hash]' width="100%" height="600"></iframe>
        </div>
      </main>
    )
}