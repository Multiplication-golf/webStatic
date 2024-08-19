{ pkgs }: {
  deps = [
    pkgs.geckodriver
    pkgs.lsof
    pkgs.nodePackages.vscode-langservers-extracted
    pkgs.nodePackages.typescript-language-server
  ];
}