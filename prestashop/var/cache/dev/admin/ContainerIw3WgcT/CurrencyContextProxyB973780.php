<?php

namespace ContainerIw3WgcT;

class CurrencyContextProxyB973780 extends \PrestaShop\PrestaShop\Core\Context\CurrencyContext implements \Symfony\Component\VarExporter\LazyObjectInterface
{
    use \Symfony\Component\VarExporter\LazyProxyTrait;

    private const LAZY_OBJECT_PROPERTY_SCOPES = [
        "\0".'*'."\0".'id' => [parent::class, 'id', null, 8],
        "\0".'*'."\0".'isoCode' => [parent::class, 'isoCode', null, 8],
        "\0".'*'."\0".'localizedNames' => [parent::class, 'localizedNames', null, 8],
        "\0".'*'."\0".'localizedPatterns' => [parent::class, 'localizedPatterns', null, 8],
        "\0".'*'."\0".'localizedSymbols' => [parent::class, 'localizedSymbols', null, 8],
        "\0".'*'."\0".'name' => [parent::class, 'name', null, 8],
        "\0".'*'."\0".'numericIsoCode' => [parent::class, 'numericIsoCode', null, 8],
        "\0".'*'."\0".'pattern' => [parent::class, 'pattern', null, 8],
        "\0".'*'."\0".'precision' => [parent::class, 'precision', null, 8],
        "\0".'*'."\0".'symbol' => [parent::class, 'symbol', null, 8],
        "\0".parent::class."\0".'conversionRate' => [parent::class, 'conversionRate', null, 16],
        'conversionRate' => [parent::class, 'conversionRate', null, 16],
        'id' => [parent::class, 'id', null, 8],
        'isoCode' => [parent::class, 'isoCode', null, 8],
        'localizedNames' => [parent::class, 'localizedNames', null, 8],
        'localizedPatterns' => [parent::class, 'localizedPatterns', null, 8],
        'localizedSymbols' => [parent::class, 'localizedSymbols', null, 8],
        'name' => [parent::class, 'name', null, 8],
        'numericIsoCode' => [parent::class, 'numericIsoCode', null, 8],
        'pattern' => [parent::class, 'pattern', null, 8],
        'precision' => [parent::class, 'precision', null, 8],
        'symbol' => [parent::class, 'symbol', null, 8],
    ];

    public function getId(): int
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getId(...\func_get_args());
        }

        return parent::getId(...\func_get_args());
    }

    public function getName(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getName(...\func_get_args());
        }

        return parent::getName(...\func_get_args());
    }

    public function getLocalizedNames(): array
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getLocalizedNames(...\func_get_args());
        }

        return parent::getLocalizedNames(...\func_get_args());
    }

    public function getIsoCode(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getIsoCode(...\func_get_args());
        }

        return parent::getIsoCode(...\func_get_args());
    }

    public function getNumericIsoCode(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getNumericIsoCode(...\func_get_args());
        }

        return parent::getNumericIsoCode(...\func_get_args());
    }

    public function getConversionRate(): \PrestaShop\Decimal\DecimalNumber
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getConversionRate(...\func_get_args());
        }

        return parent::getConversionRate(...\func_get_args());
    }

    public function getSymbol(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getSymbol(...\func_get_args());
        }

        return parent::getSymbol(...\func_get_args());
    }

    public function getLocalizedSymbols(): array
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getLocalizedSymbols(...\func_get_args());
        }

        return parent::getLocalizedSymbols(...\func_get_args());
    }

    public function getPrecision(): int
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getPrecision(...\func_get_args());
        }

        return parent::getPrecision(...\func_get_args());
    }

    public function getPattern(): string
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getPattern(...\func_get_args());
        }

        return parent::getPattern(...\func_get_args());
    }

    public function getLocalizedPatterns(): array
    {
        if (isset($this->lazyObjectState)) {
            return ($this->lazyObjectState->realInstance ??= ($this->lazyObjectState->initializer)())->getLocalizedPatterns(...\func_get_args());
        }

        return parent::getLocalizedPatterns(...\func_get_args());
    }
}

// Help opcache.preload discover always-needed symbols
class_exists(\Symfony\Component\VarExporter\Internal\Hydrator::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectRegistry::class);
class_exists(\Symfony\Component\VarExporter\Internal\LazyObjectState::class);

if (!\class_exists('CurrencyContextProxyB973780', false)) {
    \class_alias(__NAMESPACE__.'\\CurrencyContextProxyB973780', 'CurrencyContextProxyB973780', false);
}
