import { JSX } from "react";
import { ChatMessage } from "../types/ChatMessage";
import LLMMessage from "./LLMResponse";
import UserMessage from "./UserQuery";


interface ChatBubbleProps {
  message: ChatMessage;
}

export default function ChatBubble({message}: ChatBubbleProps): JSX.Element {
  if (message.isUser) {
    return <UserMessage message={message} />;
  }
  return <LLMMessage message={message} />;
}
