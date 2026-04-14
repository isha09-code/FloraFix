// Handle payment submission
document.addEventListener("DOMContentLoaded", () => {
  const paymentForm = document.getElementById("payment-form");
  const status = document.getElementById("payment-status");

  if (paymentForm) {
    paymentForm.addEventListener("submit", (e) => {
      e.preventDefault();

      // Simulate payment success
      status.textContent = "✅ Payment Successful! Subscription Activated.";
      status.classList.add("text-green-400");

      // Redirect back to subscription page
      setTimeout(() => {
        window.location.href = "subscription.html";
      }, 3000);
    });
  }
});