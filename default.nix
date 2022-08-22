{ pkgs ? import <nixpkgs> {} }:
let
  mach-nix = import (builtins.fetchGit {
    url = "https://github.com/DavHau/mach-nix/";
    ref = "refs/tags/3.5.0";
  }) {};
  python = mach-nix.mkPython {
    requirements = builtins.readFile ./requirements.txt;
  };
  package = { lib, python3Packages }:
  python3Packages.buildPythonPackage {
    name = "faucet";
    src = ./.;

    propagatedBuildInputs = [ python ];

    installPhase = ''
      runHook preInstall
      mkdir -p $out/${python.sitePackages}
      cp -r . $out/${python.sitePackages}/faucet
      runHook postInstall
    '';

    shellHook = "export FLASK_APP=faucet.py";

    format = "other";
  };
in
pkgs.callPackage package {}
