import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-white shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <div className="text-xl font-semibold text-emerald-600">
              My Newsletter
            </div>
          </div>
          <div className="flex items-center space-x-8">
            <Link 
              to="/" 
              className="text-gray-700 hover:text-emerald-600 px-3 py-2 rounded-md text-sm font-medium"
            >
              Home
            </Link>
            <Link 
              to="/newsletters" 
              className="text-gray-700 hover:text-emerald-600 px-3 py-2 rounded-md text-sm font-medium"
            >
              Newsletter
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar; 