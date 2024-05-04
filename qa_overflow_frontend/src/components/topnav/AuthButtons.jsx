import BaseButton from "../base/BaseButtons";

export default function AuthButtons() {
    return (
        <div className="flex flex-row space-x-3">
            <BaseButton content="Login" bg="while" border="darkblue" text="blue" />
            <BaseButton content="Register" bg="darkblue" border="blue" text="white" />
        </div>
    )
}