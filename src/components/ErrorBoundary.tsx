import React, { useState, useEffect, ReactNode } from "react";

interface Props {
  children: ReactNode;
}

export default function ErrorBoundary({ children }: Props) {
  const [hasError, setHasError] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    const errorHandler = (e: ErrorEvent) => {
      setHasError(true);
      setError(e.error);
    };

    const rejectionHandler = (e: PromiseRejectionEvent) => {
      setHasError(true);
      setError(e.reason);
    };

    window.addEventListener("error", errorHandler);
    window.addEventListener("unhandledrejection", rejectionHandler);

    return () => {
      window.removeEventListener("error", errorHandler);
      window.removeEventListener("unhandledrejection", rejectionHandler);
    };
  }, []);

  if (hasError) {
    let errorMessage = "Something went wrong.";
    try {
      // Check if it's a Firestore JSON error
      const parsed = JSON.parse(error?.message || "");
      if (parsed.error && parsed.operationType) {
        errorMessage = `Database Error: ${parsed.error} during ${parsed.operationType} operation.`;
      }
    } catch (e) {
      // Not a JSON error, use the raw message
      errorMessage = error?.message || errorMessage;
    }

    return (
      <div className="min-h-screen flex items-center justify-center bg-zinc-50 px-4">
        <div className="max-w-md w-full bg-white p-8 rounded-2xl border border-black/5 shadow-sm text-center space-y-4">
          <h2 className="text-2xl font-bold text-zinc-900 font-display">Oops!</h2>
          <p className="text-zinc-600">{errorMessage}</p>
          <button
            onClick={() => window.location.reload()}
            className="px-6 py-2 bg-emerald-600 text-white rounded-full font-medium hover:bg-emerald-700 transition-colors"
          >
            Reload Page
          </button>
        </div>
      </div>
    );
  }

  return <>{children}</>;
}
