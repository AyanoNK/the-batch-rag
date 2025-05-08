import { JSX } from "react";
import { ChatMessage } from "../types/ChatMessage";
import Markdown from "react-markdown";

interface LLMMessageProps {
  message: ChatMessage;
}

export default function LLMMessage({ message }: LLMMessageProps): JSX.Element {
  return (
    <div className="flex w-full justify-start">
      <div className="max-w-md rounded-t-lg rounded-br-lg border border-b-cyan-800 p-4">
        <span className="whitespace-pre-line">
          <Markdown>{message.text}</Markdown>
        </span>
      </div>
    </div>
  );
}
