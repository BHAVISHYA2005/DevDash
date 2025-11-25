import { Button } from "@/components/ui/button";
import { Home, BarChart3, Settings, Users, FileText } from "lucide-react";

export default function Sidebar() {
  return (
    <aside className="w-64 bg-white border-r border-border flex flex-col">
      <div className="p-6 border-b border-border">
        <h1 className="text-2xl font-bold text-primary">DevDash</h1>
        <p className="text-sm text-muted-foreground">Developer Dashboard</p>
      </div>

      <nav className="flex-1 p-4 space-y-2">
        <Button variant="ghost" className="w-full justify-start gap-3">
          <Home className="h-5 w-5" />
          Dashboard
        </Button>
        <Button variant="ghost" className="w-full justify-start gap-3">
          <BarChart3 className="h-5 w-5" />
          Analytics
        </Button>
        <Button variant="ghost" className="w-full justify-start gap-3">
          <Users className="h-5 w-5" />
          Team
        </Button>
        <Button variant="ghost" className="w-full justify-start gap-3">
          <FileText className="h-5 w-5" />
          Projects
        </Button>
        <Button variant="ghost" className="w-full justify-start gap-3">
          <Settings className="h-5 w-5" />
          Settings
        </Button>
      </nav>
    </aside>
  );
}