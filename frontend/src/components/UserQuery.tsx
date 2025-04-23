import { ChatMessage } from "../types/ChatMessage";

interface UserMessageProps {
  message: ChatMessage;
}

export default function UserMessage({ message }: UserMessageProps) {
  return (
    <div className="flex w-full justify-end">
      <div className="max-w-md rounded-t-lg rounded-bl-lg border border-b-cyan-800 p-4">
        <span>{message.text}</span>
      </div>
    </div>
  );
}
