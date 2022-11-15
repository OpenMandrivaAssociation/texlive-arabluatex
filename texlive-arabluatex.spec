Name:		texlive-arabluatex
Version:	54512
Release:	1
Summary:	ArabTeX for LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/arabluatex
License:	gpl3+ cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabluatex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabluatex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabluatex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides for LuaLaTeX an ArabTeX-like interface to
generate Arabic writing from an ascii transliteration. It is
particularly well-suited for complex documents such as
technical documents or critical editions where a lot of
left-to-right commands intertwine with Arabic writing.
arabluatex is able to process any ArabTeX input notation. Its
output can be set in the same modes of vocalization as ArabTeX,
or in different roman transliterations. It further allows many
typographical refinements. It will eventually interact with
some other packages yet to come to produce from .tex source
files, in addition to printed books, TEI xml compliant critical
editions and/or lexicons that can be searched, analyzed and
correlated in various ways.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/lualatex/arabluatex
%{_texmfdistdir}/tex/lualatex/arabluatex
%doc %{_texmfdistdir}/doc/lualatex/arabluatex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
