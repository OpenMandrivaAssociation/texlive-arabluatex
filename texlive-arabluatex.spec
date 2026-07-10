%global tl_name arabluatex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.20
Release:	%{tl_revision}.1
Summary:	ArabTeX for LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/arabluatex
License:	gpl3+ cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arabluatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arabluatex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arabluatex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides for LuaLaTeX an ArabTeX-like interface to generate
Arabic writing from an ascii transliteration. It is particularly well-
suited for complex documents such as technical documents or critical
editions where a lot of left-to-right commands intertwine with Arabic
writing. arabluatex is able to process any ArabTeX input notation. Its
output can be set in the same modes of vocalization as ArabTeX, or in
different roman transliterations. It further allows many typographical
refinements. It will eventually interact with some other packages yet to
come to produce from .tex source files, in addition to printed books,
TEI xml compliant critical editions and/or lexicons that can be
searched, analyzed and correlated in various ways.

