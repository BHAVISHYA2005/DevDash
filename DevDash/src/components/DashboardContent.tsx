import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Table } from "@/components/ui/table";

export default function DashboardContent() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
      <Card>
        <h2 className="text-lg font-bold mb-2">Welcome to DevDash</h2>
        <Button>Get Started</Button>
      </Card>
      <Card>
        <h2 className="text-lg font-bold mb-2">Analytics</h2>
  <Table></Table>
      </Card>
    </div>
  );
}