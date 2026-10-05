// Tebex webstore public token (Tebex panel -> Integrations -> Headless API). Empty = the catalogue below is shown
// with "Opening soon" buttons. With a token the packages come live from Tebex (create them as in TEBEX-PAKETE.md).
// The catalogue mirrors the Tebex packages: keep names and prices in sync with the panel.
window.VALHALLA_STORE = {
  token: "14t67-f2a154c49c23027e70f1aaeeb580101ca80100ef",
  currency: "USD",
  // Paused after the Tebex review: future commissions need individually specified packages.
  unavailablePackageIds: [7711510, 7711610, 7711511, 7711512],
  catalogue: [
    {category: "Ranks", packages: [
      {name: "VIP Member (Permanent)", price: "30.00", featured: true, perks: [
        "+10,000 RM on the character you play",
        "4 character slots instead of 2",
        "Luftwaffe and Kriegsmarine factions unlocked",
        "Physgun, toolgun and props (PET) right away",
        "VIP tools: Advanced Duplicator, bodygroups, lights, lamps",
        "+25 % pay; vehicle flags are not included",
        "VIP tag in chat, reserved slot when the server is full",
        "VIP role on our Discord, may apply for Trusted"],
        note: "PET can be taken away for abuse (prop climbing, spam, blocking, killing)."},
      {name: "[BUNDLE] VIP & Vehicle Flags", price: "39.00", perks: [
        "Everything in VIP Member",
        "Permanent vehicle flags",
        "Separately 50.00"]}
    ]},
    {category: "Flags", packages: [
      {name: "PET Flags", price: "10.00", perks: ["Physgun, toolgun and props", "Permanent, on every character"],
        note: "Taken away for abuse, no refund for abuse."},
      {name: "Vehicle Flags", price: "20.00", perks: [
        "Spawn period vehicles from the Q menu",
        "Civilians: civilian section; government factions: government section too",
        "Disabled while more than 100 players are online"],
        note: "Abuse (escaping roleplay, unfitting vehicles, throwing vehicles) removes them."},
      {name: "Black Market Flags", price: "15.00", perks: [
        "Black market tab in the business menu",
        "17 weapons to sell, from the spade to the MP40"],
        note: "Taken away for abuse."}
    ]},
    {category: "Attachments", packages: [
      {name: "Permanent Attachments - Scopes", price: "12.00", perks: [
        "Scoped rifles at the quartermaster regardless of rank",
        "Kar98k, G43, Springfield and Lee Enfield with scope"]},
      {name: "Permanent Attachments - Camo & More", price: "10.00", perks: [
        "Woodland camouflage on MP40, StG44, MG42, MG34, Kar98k, G43 and FG42"]},
      {name: "Permanent Attachments - Rifles", price: "6.00", perks: [
        "Kar98k, Lee Enfield, Springfield: +15 % rate of fire",
        "20 % faster bolt and reload"]},
      {name: "Permanent Attachments - Pistols", price: "6.00", perks: [
        "Every pistol: 20 % less recoil, +25 % range, +10 % rate of fire"]},
      {name: "Permanent Attachments - Ammo", price: "4.00", perks: [
        "Match ammunition: less recoil and spread, +10 % range",
        "or magnum: +10 % damage, more recoil (switch with /ammotype)"]}
    ]},
    {category: "Weapons", note: "You spawn with the item on every character. The RDM rules still apply.", packages: [
      {name: "Permanent Cigarette", price: "2.00", perks: ["A cigarette on every spawn"]},
      {name: "Permanent Camera", price: "5.00", perks: ["Camera with flash on every spawn"]},
      {name: "Permanent Walther P38", price: "12.00", perks: ["Walther P38 with a loaded magazine on every spawn"]},
      {name: "Permanent Walther PPK", price: "12.00", perks: ["Compact Walther PPK with a loaded magazine"]},
      {name: "Permanent Revolver", price: "12.00", perks: ["Webley Mk.IV revolver, loaded"]},
      {name: "Permanent Welrod", price: "9.00", perks: ["Welrod, suppressed bolt-action pistol, loaded"]},
      {name: "Permanent Knife", price: "5.00", perks: ["Combat knife (marine bayonet): quick and strong stab"]},
      {name: "Permanent Axe", price: "5.00", perks: ["Axe on every spawn"]},
      {name: "Permanent Spade", price: "5.00", perks: ["Entrenching tool, legal to carry"]},
      {name: "Permanent Bayonet", price: "7.00", perks: ["Marine bayonet on every spawn"]},
      {name: "Permanent Frying Pan", price: "5.00", perks: ["Frying pan, legal to carry"]},
      {name: "Permanent Crowbar", price: "5.00", perks: ["Crowbar, legal to carry (no lockpick)"]}
    ]},
    {category: "Characters", packages: [
      {name: "Luftwaffe Whitelist", price: "8.00", perks: ["Create Luftwaffe characters"]},
      {name: "Kriegsmarine Whitelist", price: "8.00", perks: ["Create Kriegsmarine characters"]}
    ]},
    {category: "Other", packages: [
      {name: "+1 Character Slot", price: "5.00", perks: ["One more character slot per purchase", "Requires VIP"]},
      {name: "10,000 RM Cash Package", price: "10.00", perks: ["+10,000 RM on the character you play"]},
      {name: "Locked Storage (20 Slots)", price: "10.00", perks: ["Lockable container with 20 slots", "Placed by our staff, you choose the password"]}
    ]},
    {category: "Specials", packages: [
      {name: "Founder Medal", price: "49.00", perks: ["Founder's Badge on every character", "Shown in the medal case and above your name"]}
    ]}
  ]
};
