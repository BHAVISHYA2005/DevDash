import Sidebar from './components/Sidebar';
import Navbar from './components/Navbar';
import DashboardContent from './components/DashboardContent';

function App() {
  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar />
      <div className="flex flex-col flex-1">
        <Navbar />
        <main className="p-4 flex-1 overflow-y-auto">
          <DashboardContent />
        </main>
      </div>
    </div>
  );
}

export default App;