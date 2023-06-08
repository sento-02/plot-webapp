import React from 'react'
interface InputProps {
    value: string
    checked: boolean
    handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void
}
export const InputCheckboxChild = ({value, checked, handleChange }: InputProps) => {
    return (
        <>
        <input
            type="checkbox"
            value={value}
            checked={checked}
            onChange={(e) => handleChange(e)}
        />
        </>
    )
}