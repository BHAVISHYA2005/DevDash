import { Button } from "@/components/ui/button";
import { Avatar } from "@/components/ui/avatar";

export default function Navbar() {
  return (
    <nav className="flex items-center justify-between h-16 px-6 bg-white border-b border-border">
      <div className="font-bold text-xl">DevDash</div>
      <div className="flex items-center gap-4">
        <Button variant="outline">Notifications</Button>
        <Avatar>
          
        </Avatar>
      </div>
    </nav>
  );
}