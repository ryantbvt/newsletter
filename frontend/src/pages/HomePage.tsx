import { Link } from "react-router-dom";

export default function HomePage() {
  return (
    <main className="absolute inset-0 top-0 flex flex-col items-center justify-center px-4 overflow-hidden">
      <div className="text-center max-w-2xl mt-16">
        <h1 className="font-bold text-5xl mb-8 text-gray-800 tracking-tight">
          Welcome to <span className="text-emerald-600">Newsletter</span>
        </h1>
        <p className="text-xl mb-10 text-gray-600 leading-relaxed">
          Your platform for creating and sharing amazing content. Start your writing journey today.
        </p>
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <Link 
            to="/newsletters" 
            className="inline-flex items-center px-6 py-3 rounded-full bg-emerald-500 text-white font-medium hover:bg-emerald-600 transition-all shadow-lg hover:shadow-xl transform hover:-translate-y-1"
          >
            View Newsletters
          </Link>
          <Link 
            to="/create-post" 
            className="inline-flex items-center px-6 py-3 rounded-full bg-white text-emerald-500 border border-emerald-500 font-medium hover:bg-emerald-50 transition-all shadow-lg hover:shadow-xl transform hover:-translate-y-1"
          >
            Create New Post
          </Link>
        </div>
      </div>
    </main>
  );
} 