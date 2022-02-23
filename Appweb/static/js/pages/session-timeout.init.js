$.sessionTimeout({
  keepAliveUrl: "utility_starterpage",
  logoutButton: "logout",
  logoutUrl: "authentication_login",
  redirUrl: "authentication_lockscreen",
  warnAfter: 3e3,
  redirAfter: 3e4,
  countdownMessage: "Redirecting in {timer} seconds.",
}),
  $("#session-timeout-dialog  [data-dismiss=modal]").attr(
    "data-bs-dismiss",
    "modal"
  );
  
