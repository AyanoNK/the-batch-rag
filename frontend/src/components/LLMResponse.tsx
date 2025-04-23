import { JSX } from "react";
import { ChatMessage } from "../types/ChatMessage";

interface LLMMessageProps {
  message: ChatMessage;
}

export default function LLMMessage({ message }: LLMMessageProps): JSX.Element {
  return (
    <div className="flex w-full justify-start">
      <div className="max-w-md rounded-t-lg rounded-br-lg border border-b-cyan-800 p-4">
        <span>{message.text}</span>
      </div>
    </div>
  );
}
