import { Button } from "@/components/ui/button";

export default function Navbar() {
  return (
    <div className="h-16 bg-white shadow flex items-center px-4">
      <Button variant="ghost">Dashboard</Button>
      <Button variant="ghost">Analytics</Button>
      <Button variant="ghost">Settings</Button>
      
    </div>
  );
}